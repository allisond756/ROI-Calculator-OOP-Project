from __future__ import division
class ROIcalculator():

    def __init__(self, yearlyIncome, yearlyExpenses, yearly_cash_flow):
        self.yearlyIncome = yearlyIncome
        self.yearlyExpenses = yearlyExpenses
        self.yearly_cash_flow = yearly_cash_flow

    def findMonthlyIncome(self, monthly_income = []):
        rental_income = input("Enter monthly rent")
        monthly_income.append(int(rental_income))
        laundry_income = input("Enter monthly laundry income")
        monthly_income.append(int(laundry_income))
        storage_income = input("Enter monthly storage income")
        monthly_income.append(int(storage_income))
        misc_income = input("Enter any miscellaneous income")
        monthly_income.append(int(misc_income))
        total_monthly_income = sum(monthly_income)
        self.yearlyIncome = total_monthly_income * 12
        print(f"Yearly income: {self.yearlyIncome}")
    
    def findMonthlyExpenses(self, monthly_expenses = []):
        taxes = input("Enter monthly taxes")
        monthly_expenses.append(int(taxes))
        insurance = input("Enter monthly insurance costs")
        monthly_expenses.append(int(insurance))
        electric = input("Enter monthly electric costs")
        monthly_expenses.append(int(electric))
        water = input("Enter monthly water costs")
        monthly_expenses.append(int(water))
        sewer = input("Enter monthly sewer costs")
        monthly_expenses.append(int(sewer))
        trash = input("Enter monthly trash collection costs")
        monthly_expenses.append(int(trash))
        gas = input("Enter monthly gas costs")
        monthly_expenses.append(int(gas))
        hoa = input("Enter monthly H.O.A. costs")
        monthly_expenses.append(int(hoa))
        landscape = input("Enter monthly landscaping costs")
        monthly_expenses.append(int(landscape))
        vacancy = input("Enter monthly vacancy costs")
        monthly_expenses.append(int(vacancy))
        repairs = input("Enter monthly repair costs")
        monthly_expenses.append(int(repairs))
        capex = input("Enter monthly CapEx costs")
        monthly_expenses.append(int(capex))
        mortgage = input("Enter monthly mortgage costs")
        monthly_expenses.append(int(mortgage))
        property_management = input("Enter monthly property management costs")
        monthly_expenses.append(int(property_management))
        total_monthly_expenses = sum(monthly_expenses)
        self.yearlyExpenses = total_monthly_expenses * 12
        print(f"Yearly expenses: {self.yearlyExpenses}")

    def findCashFlow(self):
        self.yearly_cash_flow = self.yearlyIncome - self.yearlyExpenses
        print(f"Yearly cash flow: {self.yearly_cash_flow}")

    def findCashOnCashROI(self, home_investement = [],):
        down_payment = input("Enter down payment cost")
        home_investement.append(int(down_payment))
        closing_cost = input("Enter closing costs")
        home_investement.append(int(closing_cost))
        rehab_budget = input("Enter renovation costs")
        home_investement.append(int(rehab_budget))
        misc_costs = input("Enter any miscellaneous home costs")
        home_investement.append(int(misc_costs))
        total_investement = sum(home_investement)
        print(f"Your total investment: {total_investement}")
        roi_num = self.yearly_cash_flow / total_investement
        print(self.yearly_cash_flow)
        roi_percent = roi_num * 100
        print(f"Your Cash on Cash ROI is: {roi_percent}% ")


new_home = ROIcalculator([],[],[])

def runCalculator():
    new_home.findMonthlyIncome()
    new_home.findMonthlyExpenses()
    new_home.findCashFlow()
    new_home.findCashOnCashROI([])

runCalculator()

