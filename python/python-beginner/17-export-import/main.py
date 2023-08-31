import bank_account
import helper_function

feri_szamlaja = bank_account.BankAccount("Feri", 25000, [20000, -15000, -2000, 25000, -5000])

feri_szamlaja.account_details()
helper_function.t_actions(feri_szamlaja.action)
helper_function.full_release(feri_szamlaja.action)
helper_function.income(feri_szamlaja.action)
