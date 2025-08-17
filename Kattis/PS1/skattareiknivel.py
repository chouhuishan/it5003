from math import floor


def get_net_annual_salary(L: float, s: float, salaries: list[int]) -> int:
    pension_fund_pct = L / 100
    private_prop_pct = s / 100
    monthly_tax_exemption = 59_665
    updated_tax_exemption = monthly_tax_exemption
    net_annual_salary = 0
    tax_bracket_ceiling_1 = 409_986
    tax_bracket_ceiling_2 = 1_151_012
    tax_brackets = {1: 0.3145, 2: 0.3795, 3: 0.4625}

    for salary in salaries:
        tax_base = (
            salary - floor(salary * pension_fund_pct) - floor(salary * private_prop_pct)
        )

        if tax_base <= tax_bracket_ceiling_1:
            withholding_tax = floor(tax_base * tax_brackets[1])
        elif tax_base <= tax_bracket_ceiling_2:
            withholding_tax = floor(
                tax_bracket_ceiling_1 * tax_brackets[1]
                + (tax_base - tax_bracket_ceiling_1) * tax_brackets[2]
            )
        else:
            withholding_tax = floor(
                tax_bracket_ceiling_1 * tax_brackets[1]
                + (tax_bracket_ceiling_2 - tax_bracket_ceiling_1) * tax_brackets[2]
                + (tax_base - tax_bracket_ceiling_2) * tax_brackets[3]
            )

        if withholding_tax < updated_tax_exemption:
            carried_forward_tax_exemption = updated_tax_exemption - withholding_tax
            tax_payable = 0
        else:
            tax_payable = withholding_tax - updated_tax_exemption
            carried_forward_tax_exemption = 0

        updated_tax_exemption = monthly_tax_exemption + carried_forward_tax_exemption
        net_annual_salary += tax_base - tax_payable

    return net_annual_salary


L = float(input())  # contribution % to pension fund
s = float(input())  # contribution % to private property fund
salaries = [int(input()) for _ in range(12)]  # 12 months = 1 year

print(get_net_annual_salary(L, s, salaries))
