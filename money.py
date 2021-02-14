'''
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
'''
save_money=1000
def send_money(pay):
    int_new_money=save_money+pay
    return int_new_money
def select_money(pay):
    print(f"当前工资数额:{pay}")
    return pay
if __name__ == '__main__':
    select_money(save_money)
    select_money(send_money(1000))