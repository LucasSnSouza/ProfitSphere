from services.responder_service import Responder
from services.employee_service import EmployeeService

class EmployeeController():
    
    def __init__(self):
        self.employee_service = EmployeeService()