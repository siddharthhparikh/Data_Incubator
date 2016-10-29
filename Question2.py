import csv

def find_median(duration, total_records):
	current_records = 0
	median = list()
	flag = True
	for i in range(duration['min'], duration['max']+1):
		if duration.has_key(i):
			#print i, duration[i]
			if not flag:
				median.append(i)
				return median
			elif current_records+duration[i] == float(total_records)/2:
				median.append(i)
				flag = False
			elif current_records+duration[i] > float(total_records)/2:
				median.append(i)
				print current_records+duration[i], total_records
				return median
			current_records = current_records + duration[i]

def calculate_mean_duration():
	duration = {}
	total_records = 0
	max_time = 0
	min_time = 999999
	for i in range(1,13):
		name = '0' + str(i)
		with open('../2015'+name[-2:]+'-citibike-tripdata.csv', 'r') as csvfile:
			csvfile.readline()
			rdr = csv.reader(csvfile, delimiter=',')
			for row in rdr:
				
				d = int(row[0])
				if d > max_time:
					max_time = d
				if d < min_time:
					min_time = d
				if duration.has_key(d):
					duration[d] = duration[d]+1
				else:
					duration[d] = 1
				
				total_records = total_records+1
	
	duration['min'] = min_time
	duration['max'] = max_time

	median = find_median(duration, total_records)
	print median, total_records

def fraction_rides():
	total = 0
	same_id = 0
	for i in range(1,13):
		name = '0' + str(i)
		with open('../2015'+name[-2:]+'-citibike-tripdata.csv', 'r') as csvfile:
			csvfile.readline()
			rdr = csv.reader(csvfile, delimiter=',')
			for row in rdr:
				if row[3] == row[7]:
					same_id = same_id +1
				total = total + 1
	print same_id, total
	print float(same_id)/total

def std_bike_stations():
	bikes = {}
	for i in range(1,13):
		name = '0' + str(i)
		with open('../2015'+name[-2:]+'-citibike-tripdata.csv', 'r') as csvfile:
			csvfile.readline()
			rdr = csv.reader(csvfile, delimiter=',')
			for row in rdr:
				if bikes.has_key(row[11]):
					if not bikes[row[11]].has_key(row[3]):	
						bikes[row[11]][row[3]] = True
					if not bikes[row[11]].has_key(row[7]):	
						bikes[row[11]][row[7]] = True
				else:
					bikes[row[11]] = {}
					bikes[row[11]][row[3]] = True
					bikes[row[11]][row[7]] = True

	#for mean
	mean = 0
	for key, value in bikes:
		mean = mean + len(value)
	mean = mean/len(bikes)
	print mean

def main():
	#calculate_mean_duration()
	#fraction_rides()
	std_bike_stations()
if __name__ == '__main__':
	main()