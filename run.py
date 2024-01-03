import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def get_sales_data():

    """
    Get sales figures input from the user
    """
    print("Please enter sales data from the last marker")
    print("Data should be six numbers, separated by commas")
    print("Example: 10, 20, 30, 40, 50, 60")

    data_str = input("Enter your data here: ")

    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    """
    Inside the Try, converts all string values into integers.
    Raises ValueError if strings cannot be converted to Int.
    Or if there aren't six values.
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly six values required, you entered {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

get_sales_data()
