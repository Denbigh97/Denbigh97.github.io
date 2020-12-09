console.log("Hello")
console.log(data)

console.log()

let trace1  = {
    x: data.map(d => d.TEAM_ABBREVIATION),
    y: data.map(d => d.PTS),
    name: 'avg pts year'
};

let trace2  = {
    x: data.map(d => d.TEAM_ABBREVIATION),
    y: data.map(d => d.SEASON_ID),
    name: 'teams'
};

let trace3  = {
    x: data.map(d => d.TEAM_ABBREVIATION),
    y: data.map(d => d.Is_Win),
    name: 'wins'
};

let plotData = [trace1, trace2, trace3]

let plotLayout = {
    title: "NBA STATS"
};
  
  
Plotly.newPlot('myPlot', plotData);


