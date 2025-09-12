test_cases = int(input())
for _ in range(test_cases):
    cars = int(input())
    num_requests = int(input())

    requests_by_id = {}
    for i in range(1, cars+1):
        requests_by_id[i] = []
    for _ in range(num_requests):
        client, start, end, id_model = input().split()
        client = int(client)
        id_model = int(id_model)
        start = int(start.split(':')[0]) * 60 + int(start.split(':')[1])
        end = int(end.split(':')[0]) * 60 + int(end.split(':')[1])

        request = (start, end, client)
        requests_by_id[id_model].append(request)
    s_requests_by_id = sorted(requests_by_id.items())
    results = []
    for id_model, requests in s_requests_by_id:
        requests.sort(key=lambda x: (x[1], x[0]))
        clients = []
        last_return = -1
        for start, end, client in requests:
            if start >= last_return:
                clients.append(client)
                last_return = end
        
        if clients:        
            results.append(f"{id_model}: {len(clients)} = {', '.join(map(str, clients))}")
        else:
             results.append(f"{id_model}: {len(clients)}")
    print(" | ".join(results))
       



    

