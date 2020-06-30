

$(document).ready(function () {
    function getDailyTasksOnSuccess(days) {

        var contentContainer = $('#content');
        var iteration = 0;

        for (var day in days) {
            for (var task in days[day]) {


                var templateContainerId = 'template-container-' + iteration++;
                var templateContainer = '<div id="' + templateContainerId + '"</div>'
                contentContainer.append(templateContainer);

                $('#' + templateContainerId).loadTemplate("webroot/js/templates/daily-task-template.html", days[day][task]);
            }
        }
    }

    $.get('/api/v1/tasks-today', getDailyTasksOnSuccess);
});