var create_project = function () {
    var pname = $("#pname").val();
    var gitaddr = $("#gitaddr").val();
    var redisdb = $("#redisdb").val();
    var fsroot = $("fsroot").val();
    var sourcelist = $("sourcelist").val();

    // aysnc call to create the project
    $.ajax({
        url: "/projects/",
        async: true,
    });
};

var clean_coverage = function () {

};
