import pandas as pd


class FlightDelayAnalyzer:

    # 1. Create Flight Log DataFrame
    def create_flight_log_df(self, flight_log: list) -> pd.DataFrame:
        return pd.DataFrame(
            flight_log,
            columns=["FlightID", "AirlineCode", "Route", "Delay"]
        )

    # 2. Create Airline Master DataFrame
    def create_airline_master_df(self, airline_master: list) -> pd.DataFrame:
        return pd.DataFrame(
            airline_master,
            columns=["AirlineCode", "AirlineName"]
        )

    # 3. Merge Airline Names into Flight Log
    def merge_airline_names(
        self,
        flight_log_df: pd.DataFrame,
        airline_master_df: pd.DataFrame
    ) -> pd.DataFrame:

        merged_df = pd.merge(
            flight_log_df,
            airline_master_df,
            on="AirlineCode",
            how="left"
        )

        return merged_df

    # 4. Calculate Average Delay per Airline
    def average_delay_by_airline(
        self,
        merged_df: pd.DataFrame
    ) -> pd.DataFrame:

        avg_delay_df = (
            merged_df.groupby("AirlineName")["Delay"]
            .mean()
            .reset_index()
            .rename(columns={"Delay": "Average Delay"})
        )

        return avg_delay_df

    # 5. Filter Flights with Delay Above Threshold
    def filter_high_delays(
        self,
        flight_log_df: pd.DataFrame,
        threshold: int
    ) -> pd.DataFrame:

        return flight_log_df[flight_log_df["Delay"] > threshold].reset_index(drop=True)

    # 6. Identify Most Delayed Route
    def most_delayed_route(
        self,
        flight_log_df: pd.DataFrame
    ) -> pd.DataFrame:

        route_delay_df = (
            flight_log_df.groupby("Route")["Delay"]
            .mean()
            .reset_index()
            .rename(columns={"Delay": "Average Delay"})
        )

        max_delay_value = route_delay_df["Average Delay"].max()

        result_df = (
            route_delay_df[
                route_delay_df["Average Delay"] == max_delay_value
            ]
            .sort_values(
                by="Average Delay",
                ascending=False
            )
            .head(1)
            .reset_index(drop=True)
        )

        return result_df
