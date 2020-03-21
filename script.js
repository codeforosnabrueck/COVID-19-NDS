/* HOW TO USE A FUNCTION

function myFunction (){
alert("hello world!");
}

myFunction();
*/


/***********************************************************************************/

// Choropleth Chart zur Zahl der Covid-19-Fälle in den einzelnen Kreisen

/***********************************************************************************/

function vis_choropleth() {
// The svg
var svg = d3.select("#vis_map"),
  width = 800,
  height = 700;

// Map and projection
var projection = d3.geoMercator()
    .translate([width / 2, height / 2])
    .scale(8000)
    .center([9.24,52.45]);

var path = d3.geoPath()
    .projection(projection);


// Data and color scale
var data = d3.map();
var colorScale = d3.scaleOrdinal().range(d3.schemeBlues[3]);




// Load external data and boot

var promises = [
  d3.json("viz/nds_kreise.geojson"),
  d3.csv("time_series/time_series_covid-19_nds_confirmed.csv", function(d) { data.set(d.code, +d.pop);})
];

Promise.all(promises).then(ready);

 function ready(fulfillmentvalue) {

  let mouseover = function(d) {
    d3.selectAll(".Country")
      .transition()
      .duration(100)
      .style("opacity", 1);
    d3.select(this)
      .transition()
      .duration(100)
      .style("opacity", 1)
      .style("stroke", "white");
      console.log(this);
      tooltip.style("display", null);


  };

  let mouseleave = function(d) {
    d3.selectAll(".Country")
      .transition()
      .duration(200)
      .style("opacity", 0.8);
    d3.select(this)
      .transition()
      .duration(200)
      .style("stroke", "transparent");
    tooltip.style("display", "none");
  };

  // Draw the map
  svg.append("g")
    .selectAll("path")
    .data(fulfillmentvalue[0].features)
    .enter()
    .append("path")
      // draw each country
      .attr("d", d3.geoPath()
        .projection(projection)
      )
      // set the color of each country
      .attr("fill", function (d) {
        d.total = data.get(d.id) || 0;
        return colorScale(d.total);
      })
      .style("stroke", "black")
      .attr("class", function(d){ return "Country"; } )
      .style("opacity", 0.5);

    }

} // end vis_choropleth

vis_choropleth();
