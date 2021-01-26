// Chart Params
var svgWidth = 960;
var svgHeight = 500;

var margin = { top: 20, right: 40, bottom: 60, left: 50 };

var chartWidth = svgWidth - margin.left - margin.right;
var chartHeight = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3
    .select("body")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);
v


// Read in the CSV file
d3.csv("data.csv").then(function (smurfData) {

    // Create a function to parse date and time
    var parseTime = d3.timeParse("%d-%b-%y");

    // Format the data to parse the date values and convert the numeric values to integers
    smurfData.forEach(function (data) {
        data.date = parseTime(data.date);
        data.dow = +data.dow_index;
        data.sightings = +data.smurf_sightings;
    });
    console.log(dow);


    // Create scaling functions (one for all 3 axes)
    var xTimeScale = d3.scaleTime()
        .domain(d3.extent(smurfData, d => d.date))
        .range([0, chartWidth]);

    var yLinearScale1 = d3.scaleLinear()
        .domain([0, d3.max(smurfData, d => d.dow)])
        .range([chartHeight, 0]);

    var yLinearScale2 = d3.scaleLinear()
        .domain([0, d3.max(smurfData, d => d.sightings)])
        .range([chartHeight, 0]);




    // Create axis functions
    var bottomAxis = d3.axisBottom(xTimeScale).tickFormat(d3.timeFormat("%d-%b-%y"));
    var leftAxis = d3.axisLeft(yLinearScale1);
    var rightAxis = d3.axisRight(yLinearScale2);



    // Create g elements and call each of the axis functions
    // Add bottomAxis
    chartGroup.append("g").attr("transform", `translate(0, ${chartHeight})`).call(bottomAxis);

    // Add leftAxis to the left side of the display
    chartGroup.append("g").call(leftAxis);

    // Add rightAxis to the right side of the display
    chartGroup.append("g").attr("transform", `translate(${chartWidth}, 0)`).call(rightAxis);


    // Create line generators (one for each line)

    var line1 = d3
        .line()
        .x(d => xTimeScale(d.date))
        .y(d => yLinearScale1(d.dow));
    console.log(line1);

    var line2 = d3
        .line()
        .x(d => xTimeScale(d.date))
        .y(d => yLinearScale2(d.sightings));


    // Append a path for line1
    chartGroup.append("path")
        .data([smurfData])
        .attr("d", line1)
        .classed("line green", true);

    // Append a path for line2
    chartGroup.append("path")
        .data([smurfData])
        .attr("d", line2)
        .classed("line orange", true);

    chartGroup.append("text")
        // Position the text
        // Center the text: (https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/text-anchor)
        .attr("transform", `translate(${chartWidth / 2}, ${chartHeight + margin.top + 10})`)
        .attr("text-anchor", "middle")
        .attr("font-size", "16px")
        .attr("fill", "green")
        .text("surfdata down");

    chartGroup.append("text")
        .attr("transform", `translate(${chartWidth / 2}, ${chartHeight + margin.top + 40})`)
        .attr("text-anchor", "middle")
        .attr("font-size", "16px")
        .attr("fill", "orange")
        .text("smurfdata sightings");

}).catch(function (error) {
    console.log(error);
});    