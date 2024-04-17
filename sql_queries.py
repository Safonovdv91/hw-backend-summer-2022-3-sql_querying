# Вывести топ 5 самых коротких по длительности перелетов.
# Duration - разница между scheduled_arrival и scheduled_departure.
# В ответе должно быть 2 колонки [flight_no, duration]
TASK_1_QUERY = """
	SELECT flight_no, ()SELECT flight_no, (scheduled_arrival - scheduled_departure) as Duration
 	FROM flights
	ORDER BY duration 
	LIMIT 5;

"""
#  flight_no | duration
# -----------+----------
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00
#  PG0233    | 00:25:00
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00


# Вывести топ 3 рейса по числу упоминаний в таблице flights
# количество упоминаний которых меньше 50
# В ответе должно быть 2 колонки [flight_no, count]
TASK_2_QUERY = """
	SELECT flight_no, count(flight_no) as count 
	FROM flights
	GROUP BY flight_no 
	HAVING count(flight_no ) < 50
	ORDER BY count(flight_no) DESC LIMIT 3;

"""
#  flight_no | count
# -----------+-------
#  PG0260    |    27
#  PG0371    |    27
#  PG0310    |    27

# Вывести число перелетов внутри одной таймзоны
# Нужно вывести 1 значение в колонке count
TASK_3_QUERY = """
select count(f.flight_no), a_dep.timezone
from flights as f
join airports_data as a_dep
ON f.departure_airport = a_dep.airport_code
join airports_data as a_arr
on f.arrival_airport = a_arr.airport_code
where a_dep.timezone = a_arr.timezone
group by a_dep.timezone order by count desc limit 1;

"""
#  count
# --------
#  16824
