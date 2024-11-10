-- Team 8 SQL Script for the Group Project
-- Durkovic Jakub N2401408A
--
--
--


-- Durkovic Jakub
# 5.For the year 2023, display the quarter-on-quarter changes in high and low prices and the quarterly average price.

with quarterly_data as (
    select 
        year(str_to_date(stockdate, '%m/%d/%Y')) as year,
        quarter(str_to_date(stockdate, '%m/%d/%Y')) as quarter,
        min(low) as minlow,
        max(high) as maxhigh,
        avg(price) as avgprice
    from 
        sia_stock
    where 
        year(str_to_date(stockdate, '%m/%d/%Y')) = 2023
    group by 
        year, quarter
)
select
    q1.year,
    q1.quarter,
    q1.minlow,
    q1.maxhigh,
    q1.avgprice,
    case 
        when q2.minlow is not null then round(((q1.minlow - q2.minlow) / q2.minlow) * 100, 2)
        else null
    end as low_price_qoq_change,
    case 
        when q2.maxhigh is not null then round(((q1.maxhigh - q2.maxhigh) / q2.maxhigh) * 100, 2)
        else null
    end as high_price_qoq_change
from 
    quarterly_data q1
left join 
    quarterly_data q2 on q1.year = q2.year and q1.quarter = q2.quarter + 1
order by 
    q1.year, q1.quarter;
    
-- Durkovic Jakub
#6. For each sales_channel and each route, display the following ratios
#      -	average length_of_stay / average flight_hour 
#      -	average wants_extra_baggage / average flight_hour
#      -	average wants_preferred_seat / average flight_hour
#      -	average wants_in_flight_meals / average flight_hour
# Our underlying objective: Are there any correlations between flight hours, length of stay,
# and various preferences (i.e., extra baggage, preferred seats, in-flight meals)?

select sales_channel, route, round(avg(length_of_stay) / avg(flight_hour), 2) as LengthOfStay, round( avg(wants_extra_baggage) / avg(flight_hour),2) as WantsExtraBaggage, round( avg(wants_preferred_seat) / avg(flight_hour),2) as PrefSeat, round(avg(wants_in_flight_meals) / avg(flight_hour),2) as WantsMeals from customer_booking
	group by sales_channel, route
    order by sales_channel asc, LengthOfStay desc;

-- Durkovic Jakub
# 7.Airline seasonality.
#For each Airline and Class, display the averages of SeatComfort, FoodnBeverages, InflightEntertainment,
# ValueForMoney, and OverallRating for the seasonal and non-seasonal periods, respectively.
select 
    airline, 
    class, 
    avg(seatcomfort) as avgseatcomfort,
    avg(foodnbeverages) as avgfoodnbeverages,
    avg(inflightentertainment) as avginflightentertainment,
    avg(valueformoney) as avgvalueformoney,
    avg(overallrating) as avgoverallrating,
    case 
        when MONTH(STR_TO_DATE(CONCAT('01-', MonthFlown), '%d-%b-%y')) in (6, 7, 8, 9) then 'seasonal' 
        else 'non-seasonal' 
    end as season
from 
    airlines_reviews
group by 
    airline, 
    class, 
    season;
    