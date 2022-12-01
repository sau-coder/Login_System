from fastapi import APIRouter , status , HTTPException
from databases.database import SessionLocal
from app.user.schema import UserLoginData
from app.user.schema import UserSignupData , ResetPasswordData
from app.user.model import UserSignup

router = APIRouter()
db = SessionLocal()


@router.post('/user_signup' , status_code = status.HTTP_201_CREATED)
def create_user(user_data : UserSignupData):

    db_entry = db.query(UserSignup).filter(UserSignup.user_name == user_data.user_name).first()

    if db_entry is not None:
        raise HTTPException (status_code=status.HTTP_400_BAD_REQUEST , detail = "User already exist.")

    db_entry = db.query(UserSignup).filter(UserSignup.email_id == user_data.email_id).first()

    if db_entry is not None:
        raise HTTPException (status_code=status.HTTP_400_BAD_REQUEST , detail = "Email already exist.")


    new_user = UserSignup(
        first_name = user_data.first_name,
        last_name = user_data.last_name,
        user_name = user_data.user_name,
        email_id = user_data.email_id,
        mobile_no = user_data.mobile_no,
        password = user_data.password,
        retype_password = user_data.retype_password
    )

    db.add(new_user)
    try:
        db.commit()
        return {'status' : status.HTTP_200_OK , 'message' : 'User created successfully'}
    except:
        db.rollback()
        return {'status' : status.HTTP_400_BAD_REQUEST , 'message' : 'rolled back due to some error'}




@router.post("/user_login" , status_code = status.HTTP_201_CREATED)
def log_in(user_data : UserLoginData):

    if user_data.type.value == "email_id":

        db_entry = db.query(UserSignup).filter(UserSignup.email_id == user_data.user).first()

        if  db_entry is None:
            raise HTTPException (status_code = status.HTTP_400_BAD_REQUEST , detail = "User not exist")

    if user_data.type.value == "user_name":

        db_entry = db.query(UserSignup).filter(UserSignup.user_name == user_data.user).first()

        if  db_entry is None:
            raise HTTPException (status_code = status.HTTP_400_BAD_REQUEST , detail = "User not exist")


    return{"status" : status.HTTP_202_ACCEPTED , "message" : "Login Successfully"}


@router.post("/forget_password" , status_code = status.HTTP_201_CREATED)
def recover_password(user_data : ResetPasswordData):
    if user_data.type.value == "email_id":

        db_entry = db.query(UserSignup).filter(UserSignup.email_id == user_data.user).first()

        if db_entry is None:
            raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST , detail = "email not found")

    if user_data.type.value == "user_name":

        db_entry = db.query(UserSignup).filter(UserSignup.user_name == user_data.user).first()

        if db_entry is None:
            raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST , detail = "user not found")


    return{"status" : status.HTTP_202_ACCEPTED , "message" : "Link has been sent to your registered Email_id or Mobile number"}


@router.delete("/delete_user/{user_name}" , status_code = status.HTTP_200_OK)
def delete_user(user_name : str):
    user_to_delete = db.query(UserSignup).filter(UserSignup.user_name == user_name).first()

    if user_to_delete is None:
        raise HTTPException (status = status.HTTP_404_NOT_FOUND , detail = "User not found")

    db.delete(user_to_delete)
    db.commit()

    return {'data' : user_to_delete , 'status' : 200 , 'message'  : 'User delete successfully'}



