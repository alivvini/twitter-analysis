let svg = d3.select("svg"),
 width = +svg.attr("width"),
 height = +svg.attr("height");

let node_data = [
    {'id': 'naruto'},
    {'id': 'sasuke'},
    {'id': 'sakura'},
    {'id': 'itachi'}
];

let node_links = [
    {'source': 'naruto', 'target': 'sasuke'},
    {'source': 'sasuke', 'target': 'sakura'},
    {'source': 'sakura', 'target': 'itachi'},
    {'source': 'itachi', 'target': 'naruto'}
];

// Setup simulation
// Nodes only for now
let simulation = d3.forceSimulation().nodes(node_data);

// Add forces
simulation
    .force("charge_force", d3.forceManyBody())
    .force("center_force", d3.forceCenter(width / 2, height / 2));

let node = svg.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(node_data)
        .enter()
        .append("circle")
        .attr("r", 5)
        .attr("fill", "red");


function tickActions() {
    //update circle positions to reflect node updates on each tick of the simulation
    node
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; })

    //update link positions
    //simply tells one end of the line to follow one node around
    //and the other end of the line to follow the other node around
    link
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });
}

simulation.on("tick", tickActions);

//Create the link force
//We need the id accessor to use named sources and targets
let link_force =  d3.forceLink(node_links)
                        .id(function(d) { return d.id; });

simulation.force("links",link_force);

//draw lines for the links
let link = svg.append("g")
      .attr("class", "links")
    .selectAll("line")
    .data(node_links)
    .enter().append("line")
      .attr("stroke-width", 2);

