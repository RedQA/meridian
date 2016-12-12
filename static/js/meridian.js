var create_project = function () {
    var pname = $("#pname").val();
    var gitaddr = $("#gitaddr").val();
    var redisdb = $("#redisdb").val();
    var drname = $("#drname").val();
    var sourcelist = $("#sourcelist").val();
    // aysnc call to create the project
    $.post("/projects/", {
        "pname": pname,
        "gitaddr": gitaddr,
        "redisdb": redisdb,
        "drname": drname,
        "sourcelist": sourcelist
    }, function (data) {
        $("#project_table tr:last").after(data);
        // hidden the dialog
        $('#myModal').modal('toggle');
    });
};

var clean_coverage = function (dom) {
    var pname = $(dom).attr("id");
    var project_clean_url = "/projects/" + pname + "/clean"
};
