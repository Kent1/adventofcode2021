with open("input.txt", 'r') as f:
    reports = [report.strip() for report in f.readlines()]
    gamma_str = ''
    for i in range(len(reports[0])):
        gamma_str += max(lst := [report[i] for report in reports], key=lst.count)
    gamma = int(gamma_str, base=2)
    epsilon = int('1' * len(gamma_str), base=2) - gamma
    print(gamma * epsilon)
    # part2
    oxy_reports = reports[:]
    co2_reports = reports[:]
    for i in range(len(reports[0])):
        if len(oxy_reports) > 1:
            oxy_criteria = max(lst := ['1', '0'] + [report[i] for report in oxy_reports], key=lst.count)
            oxy_reports = [report for report in oxy_reports if report[i] == oxy_criteria]
        if len(co2_reports) > 1:
            co2_criteria = min(lst := ['0', '1'] + [report[i] for report in co2_reports], key=lst.count)
            co2_reports = [report for report in co2_reports if report[i] == co2_criteria]
    print(int(oxy_reports[0], base=2) * int(co2_reports[0], base=2))
