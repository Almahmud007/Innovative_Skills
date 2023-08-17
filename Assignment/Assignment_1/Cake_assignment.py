import os
import sys
import time


def typr(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


typr("Welcome to Cake Point")
bf = "Black Forest"
vc = "Vanilla cake"
rv = "Red Velvet"
ls = "Lemon Sponge Cake"
cc = "Chocolate Cake"
print('\n\n')
typr(f"We have below types of cake- \n{bf} \n{vc} \n{rv} \n{ls} \n{cc}")
print('\n')

typr("#"*35)
print('\n\n')
typr("Below is the inventory cost of each item:")
print('\n')


# Raw Material Cost
inv_bf_mat = 180
inv_vc_mat = 150
inv_rv_mat = 220
inv_ls_mat = 165
inv_cc_mat = 170

# Transportation Cost
inv_trans = 150

# Space Cost
inv_spc = 50

# Staff Cost
inv_stc = 60

# Utility Cost Percentage
inv_utc = 3

# Total Inventory Cost
inv_bf_rmtc = inv_bf_mat + inv_trans
inv_bf_ttl = inv_bf_rmtc + (inv_bf_rmtc*inv_utc/100) + inv_spc + inv_stc

inv_vc_rmtc = inv_vc_mat + inv_trans
inv_vc_ttl = inv_vc_rmtc + (inv_vc_rmtc*inv_utc/100) + inv_spc + inv_stc

inv_rv_rmtc = inv_rv_mat + inv_trans
inv_rv_ttl = inv_rv_rmtc + (inv_rv_rmtc*inv_utc/100) + inv_spc + inv_stc

inv_ls_rmtc = inv_ls_mat + inv_trans
inv_ls_ttl = inv_ls_rmtc + (inv_ls_rmtc*inv_utc/100) + inv_spc + inv_stc

inv_cc_rmtc = inv_cc_mat + inv_trans
inv_cc_ttl = inv_cc_rmtc + (inv_cc_rmtc*inv_utc/100) + inv_spc + inv_stc

print(f"Inventory cost of {bf} is {inv_bf_ttl}")
print(f"Inventory cost of {vc} is {inv_vc_ttl}")
print(f"Inventory cost of {rv} is {inv_rv_ttl}")
print(f"Inventory cost of {ls} is {inv_ls_ttl}")
print(f"Inventory cost of {cc} is {inv_cc_ttl}")


typr("#"*35)
print('\n\n')
typr("Below is the selling price of each cake before discount")
print('\n')
# Selling Price
sp_bf = 780
sp_vc = 600
sp_rv = 800
sp_ls = 650
sp_cc = 660

print(f"Selling price of {bf} is {sp_bf}")
print(f"Selling price of {vc} is {sp_vc}")
print(f"Selling price of {rv} is {sp_rv}")
print(f"Selling price of {ls} is {sp_ls}")
print(f"Selling price of {cc} is {sp_cc}")


typr("#"*35)
print('\n\n')
typr("Discounted price of each cake is as per below")
print('\n')
# Discount percentage
dis_a = 5
dis_b = 7

# Price after discount
dis_sp_bf = sp_bf - (sp_bf*dis_a/100)
dis_sp_vc = sp_vc - (sp_vc*dis_a/100)
dis_sp_rv = sp_rv - (sp_rv*dis_a/100)
dis_sp_ls = sp_ls - (sp_ls*dis_b/100)
dis_sp_cc = sp_cc - (sp_cc*dis_b/100)

print(f"After discount selling price of {bf} is {dis_sp_bf}")
print(f"After discount selling price of {vc} is {dis_sp_vc}")
print(f"After discount selling price of {rv} is {dis_sp_rv}")
print(f"After discount selling price of {ls} is {dis_sp_ls}")
print(f"After discount selling price of {cc} is {dis_sp_cc}")


typr("#"*45)
print('\n\n')
typr("Total amount of sales after discount in each cake")
print('\n')

# number of sold cake
nos_bf = 5
nos_vc = 7
nos_rv = 10
nos_ls = 5
nos_cc = 9

# Total profit of each item cake

ads_total_profit_bf = (dis_sp_bf - inv_bf_ttl)*nos_bf
ads_total_profit_vc = (dis_sp_vc - inv_vc_ttl)*nos_vc
ads_total_profit_rv = (dis_sp_rv - inv_rv_ttl)*nos_rv
ads_total_profit_ls = (dis_sp_ls - inv_ls_ttl)*nos_ls
ads_total_profit_cc = (dis_sp_cc - inv_cc_ttl)*nos_cc


print(
    f"After discount total amount of profit in {bf} is {ads_total_profit_bf:.2f}")
print(
    f"After discount total amount of profit in {vc} is {ads_total_profit_vc:.2f}")
print(
    f"After discount total amount of profit in {rv} is {ads_total_profit_rv:.2f}")
print(
    f"After discount total amount of profit in {ls} is {ads_total_profit_ls:.2f}")
print(
    f"After discount total amount of profit in {cc} is {ads_total_profit_cc:.2f}")


typr("#"*35)
print('\n\n')
typr("Percentages of profit/loss")
print('\n')

# Total sales after discount of each item cake

ads_ttl_sell_bf = dis_sp_bf*nos_bf
ads_ttl_sell_vc = dis_sp_vc*nos_vc
ads_ttl_sell_rv = dis_sp_rv*nos_rv
ads_ttl_sell_ls = dis_sp_ls*nos_ls
ads_ttl_sell_cc = dis_sp_cc*nos_cc

# Total Inventory cost of each item of cake

ttl_inv_of_cake_bf = inv_bf_ttl * nos_bf
ttl_inv_of_cake_vc = inv_vc_ttl * nos_vc
ttl_inv_of_cake_rv = inv_rv_ttl * nos_rv
ttl_inv_of_cake_ls = inv_ls_ttl * nos_ls
ttl_inv_of_cake_cc = inv_cc_ttl * nos_cc


# Profit/Loss percentages
per_ttl_amount_of_profit_bf = (
    ads_ttl_sell_bf - ttl_inv_of_cake_bf)/ttl_inv_of_cake_bf*100
per_ttl_amount_of_profit_vc = (
    ads_ttl_sell_vc - ttl_inv_of_cake_vc)/ttl_inv_of_cake_vc*100
per_ttl_amount_of_profit_rv = (
    ads_ttl_sell_rv - ttl_inv_of_cake_rv)/ttl_inv_of_cake_rv*100
per_ttl_amount_of_profit_ls = (
    ads_ttl_sell_ls - ttl_inv_of_cake_ls)/ttl_inv_of_cake_ls*100
per_ttl_amount_of_profit_cc = (
    ads_ttl_sell_cc - ttl_inv_of_cake_cc)/ttl_inv_of_cake_cc*100


print(
    f"Total amount of profit percentage is {per_ttl_amount_of_profit_bf:.2f}%")
print(
    f"Total amount of profit percentage is {per_ttl_amount_of_profit_vc:.2f}%")
print(
    f"Total amount of profit percentage is {per_ttl_amount_of_profit_rv:.2f}%")
print(
    f"Total amount of profit percentage is {per_ttl_amount_of_profit_ls:.2f}%")
print(
    f"Total amount of profit percentage is {per_ttl_amount_of_profit_cc:.2f}%")
