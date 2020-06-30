

$(document).ready(function () {
    function getTasksOnSuccess(tasks, id) {

        var contentContainer = $(id);

        for (var iteration in tasks) {

            var task = tasks[iteration]
            var templateContainerId = 'template-container-' + task.id++;
            var templateContainer = '<div id="' + templateContainerId + '"</div>'
            contentContainer.append(templateContainer);

            $('#' + templateContainerId).loadTemplate("webroot/js/templates/daily-task-template.html", task);
        }
    }
    
    function today(tasks){
        getTasksOnSuccess(tasks, "#today")
    }    
    
    function tomorrow(tasks){
        getTasksOnSuccess(tasks, "#tomorrow")
    }

    $.get('/api/v1/tasks-today', today);
    $.get('/api/v1/tasks-future?count=3', tomorrow);
});