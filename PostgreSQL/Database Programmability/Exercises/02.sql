CREATE OR REPLACE FUNCTION fn_calculate_future_value(initial_sum INT,
													  yearly_interest_rate NUMERIC,
													  number_of_years INT)
RETURNS NUMERIC
AS $$
	DECLARE 
		investment NUMERIC;
	BEGIN 
		investment := initial_sum * POWER((1 + yearly_interest_rate), number_of_years);
		RETURN TRUNC(investment,4)
	END;
END;
$$
LANGUAGE plpgsql;
