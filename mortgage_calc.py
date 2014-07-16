def total_saved(monthly_sum, total_years, ror):
    year = 0
    total_sum = 0
    year_sum = monthly_sum*12
    while year <= total_years:
        year += 1
        total_sum += year_sum
        total_sum *= ror
    return total_sum

def get_monthly_payment(yearly_interest_rate, loan, years):
    monthly_interest_rate = yearly_interest_rate/12
    months = years*12
    numerator = loan*monthly_interest_rate*(monthly_interest_rate+1)**months
    denominator = (1+monthly_interest_rate)**months - 1
    monthly_payment = numerator/denominator
    return monthly_payment

def thirty_vs_fifteen(ty_interest, fy_interest, expected_ror):
    # We use 1 for house value as we're looking for relative numbers
    # instead of exact numbers
    ty_monthly = get_monthly_payment(ty_interest, 1, 30)
    fy_monthly =  get_monthly_payment(fy_interest, 1, 15)

    ty_monthly_saved = fy_monthly - ty_monthly
    ty_savings = total_saved(ty_monthly_saved,30,expected_ror)
    fy_savings = total_saved(fy_monthly,15,expected_ror)

    ty_net = ty_savings - ty_monthly*12*30 + 1
    fy_net = fy_savings - fy_monthly*12*15 + 1

    percent_benefit = int(((ty_net/fy_net) - 1) * 100)

    return percent_benefit

print str(thirty_vs_fifteen(0.042, 0.03, 1.0926)) + '%'
