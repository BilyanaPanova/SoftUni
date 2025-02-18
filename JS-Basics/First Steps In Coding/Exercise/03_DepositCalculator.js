function calculatorDeposit(deposit,term,annualInterestRate) {
    const total = deposit + (term / 100) * ((deposit * annualInterestRate)/12)

    console.log(total)
}
