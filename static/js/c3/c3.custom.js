function getGraph(month){
    $(".email_graph").each(function(){
        $.post("/graph_data/", {'data':month}, function(response){
            console.log(response);
            var data = response

            var columns = [];
            var click = data.clicks
            var open = data.open
            var x = data.dates

            console.log(x);

            columns.push(x, click, open);

            var chart = c3.generate({

                bindto: '#splineGraph',
                data: {
                    x : 'x',
                    columns: columns,

                    types: {
                        click: 'spline',
                        open: 'area-spline'
                    },
                    names: {
                        click: 'Clicks',
                        open: 'Open'
                    },
                    colors: {
                        click: '#33FF9F',
                        open: '#33D4FF'
                    }

                },
                axis: {
                    x: {
                        type: 'category',
                        tick: {
                                values: ['']
                        }
                    }
                }

            });
        });
    });
};


$(document).ready(function(){
    getGraph_by_id();
    getBasegraph();
});

function getBasegraph(){
$(".email_graph").each(function(){
        var campaign_id = $(this).attr("campaign_id");
        var campaign_type = $(this).attr("campaign_type");
        $.get("/graph_data/", function(response){
            console.log(response);
            var data = response

            var columns = [];
            var click = data.clicks
            var open = data.open
            var x = data.dates

            console.log(x);

            columns.push(x, click, open);

            var chart = c3.generate({

                bindto: '#splineGraph',
                data: {
                    x : 'x',
                    columns: columns,

                    types: {
                        click: 'spline',
                        open: 'area-spline'
                    },
                    names: {
                        click: 'Clicks',
                        open: 'Open'
                    },
                    colors: {
                        click: '#33FF9F',
                        open: '#33D4FF'
                    }

                },
                axis: {
                    x: {
                        type: 'category',
                        tick: {
                                values: ['']
                        }
                    }
                }

            });
        });
    });
}


function getGraph_by_id(){
$(".email_graph_by_id").each(function(){
        var campaign_id = $(this).attr("campaign_id");
        var campaign_type = $(this).attr("campaign_type");
        $.get("/graph_data/"+campaign_id+"/"+campaign_type, function(response){
            console.log(response);
            var data = response

            var columns = [];
            var click = data.clicks
            var open = data.open
            var x = data.dates

            console.log(x);

            columns.push(x, click, open);

            var chart = c3.generate({

                bindto: '#splineGraph',
                data: {
                    x : 'x',
                    columns: columns,

                    types: {
                        click: 'spline',
                        open: 'area-spline'
                    },
                    names: {
                        click: 'Clicks',
                        open: 'Open'
                    },
                    colors: {
                        click: '#33FF9F',
                        open: '#33D4FF'
                    }

                },
                axis: {
                    x: {
                        type: 'category',
                        tick: {
                                values: ['']
                        }
                    }
                }

            });
        });
    });
}
