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
        alert(data);
    });
};

var clean_coverage = function () {

};
