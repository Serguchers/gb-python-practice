import sys

"""Написать программу «Банковский депозит». Она должна состоять из функции и ее вызова с
аргументами. Клиент банка делает депозит на определенный срок."""

deposit_1 = {'begin_sum': 1000,
             'end_sum': 10000,
             6: 0.05,
             12: 0.06,
             24: 0.05}
deposit_2 = {'begin_sum': 10000,
             'end_sum': 100000,
             6: 0.06,
             12: 0.07,
             24: 0.065}
deposit_3 = {'begin_sum': 100000,
             'end_sum': 1000000,
             6: 0.07,
             12: 0.08,
             24: 0.075}

def deposit_counter(amount, time):
    right_depo = None
    if amount in range(deposit_1['begin_sum'], deposit_1['end_sum']):
        right_depo = deposit_1
    elif amount in range(deposit_2['begin_sum'], deposit_2['end_sum']):
        right_depo = deposit_2
    elif amount in range(deposit_3['begin_sum'], deposit_3['end_sum'] + 1):
        right_depo = deposit_3
    
    depo_final_amount = 0
    try:
        if time == 6:
            depo_final_amount = amount * (1 + right_depo[time] / 12 * time)
        elif time == 12:
            depo_final_amount = amount * (1 + right_depo[time] /12 * time)
        elif time == 24:
            depo_final_amount = amount * (1 + right_depo[time] / 12 * time)**2
        else:
            return 'Неверные параметры депозита'
    except:
        return 'Неверные параметры депозита'
    
    return depo_final_amount if depo_final_amount > 0 else 'Неверные параметры депозита'
    

if __name__ == '__main__':
    print(deposit_counter(int(sys.argv[1]), int(sys.argv[2])))
