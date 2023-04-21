import Stat from './Stat';

const Stats = () => {
    const state = {
        stats : [
            {stat_name: 'Number of Buys', stat_var: "num_buys", hasDollar: false},
            {stat_name: 'Number of Sells', stat_var: "num_sells", hasdollar: false},
            {stat_name: 'Max Buy Price', stat_var: "max_buy_price", hasDollar: true},
            {stat_name: 'Max Sell Price', stat_var: "max_sell_price", hasDollar: true},
            {stat_name: 'Last Updated', stat_var: "last_updated", hasDollar: false}
        ]
    }

    return (
        <div className='all-stats'>
            <h2>Latest Statistics</h2>
            <div className='all-stats-container'>
                {state.stats.map((stat) => (
                    <Stat stat_name={stat.stat_name} 
                    stat_var={stat.stat_var} 
                    dollar={stat.hasDollar ? "$" : ""} />
                ))}
            </div>
        </div>
    );
};

export default Stats;
