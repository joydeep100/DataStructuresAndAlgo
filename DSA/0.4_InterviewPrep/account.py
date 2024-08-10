def solution(queries):

    log = []
    accounts = {} # schema = timestamp | balance | transactions
    
    for query in queries:
        
        [task, timestamp, *args] = query
        
        # CREATE ACCOUNT FLOW
        if task == 'CREATE_ACCOUNT':
            acc_id = args[0]
            # if account is already registered
            if acc_id in accounts:
                log.append("false")
            else:
                accounts[acc_id] = {"timestamp": timestamp, "balance": 0, "transactions": 0}
                log.append("true")
            
        #DEPOSIT FLOW
        if task == 'DEPOSIT':
            acc_id = args[0]
            amount = args[1]
            # if account is not registered
            if acc_id not in accounts:
                log.append("")
            
            else:
                accounts[acc_id]["balance"] += int(amount)
                accounts[acc_id]["transactions"] += int(amount)
                accounts[acc_id]["timestamp"] = timestamp
                log.append(str(accounts[acc_id]["balance"]))
                
        #PAY FLOW
        if task == 'PAY':
            acc_id = args[0]
            amount = args[1]
            # if account is not registered
            if acc_id not in accounts:
                log.append("")
            # if we have insufficient balance
            elif int(amount) > accounts[acc_id]["balance"]:
                log.append("")
            else: 
                accounts[acc_id]["balance"] -=  int(amount)
                accounts[acc_id]["transactions"] += + int(amount)
                accounts[acc_id]["timestamp"] = timestamp
                log.append(str(accounts[acc_id]["balance"]))
                
        #TOP ACTIVITY FLOW
        elif task == 'TOP_ACTIVITY':
            count = int(args[0])
            top_transactions = sorted(accounts.items(), key=lambda item: item[1]["transactions"], reverse=True)[:count]
            res = []
            for acc_id, acc_details in top_transactions:
                res.append(f'{acc_id}({acc_details["transactions"]})')
            log.append(', '.join(sorted(res)))
            
    return log
  
queries = [["CREATE_ACCOUNT","1","accountA"], 
 ["CREATE_ACCOUNT","2","accountC"], 
 ["CREATE_ACCOUNT","3","accountB"], 
 ["DEPOSIT","4","accountA","1000"], 
 ["DEPOSIT","5","accountB","1000"], 
 ["DEPOSIT","6","accountC","1000"], 
 ["PAY","7","accountB","101"], 
 ["PAY","8","accountB","99"], 
 ["PAY","9","accountA","100"], 
 ["PAY","10","accountA","100"], 
 ["PAY","11","accountC","199"], 
 ["PAY","12","accountC","1"], 
 ["TOP_ACTIVITY","13","3"]]

print(solution(queries))