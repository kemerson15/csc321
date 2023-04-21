from pcapkit import extract

f = extract(fin='full-take.pcap', fout='weather.pcap, task.pcap')

print(f)