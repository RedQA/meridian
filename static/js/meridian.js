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
    var project_clean_url = "/projects/" + pname + "/clean/";
    $.post(project_clean_url, {}, function (data) {

    });
};

var set_pname = function (dom) {
    var pname = $(dom).attr("id");
    var button = $("#myModal2").find(".modal-footer").find("button").get(0);
    // bind the id to the button
    $(button).attr("id", pname);
};

var git_sync = function (dom) {
    var pname = $(dom).attr("id");
    var project_sync_url = "/projects/" + pname + "/gitsync/";
    var gitbranch = $("#gitbranch").val();
    $.post(project_sync_url, { "gitbranch": gitbranch }, function (data) {
        $('#myModal2').modal('toggle');
    });
};