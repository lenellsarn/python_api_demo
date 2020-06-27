

$(document).ready(function(){
    function getRawDocsOnSuccess(dictionary){

        var rawdocsContentContainer = $('#rawdocs-content');     
        var iteration = 0;  

        for(var key in dictionary) {
            var templateContainerId = 'rawdocs-template-container-' + iteration++;
            var templateContainer = '<div id="' + templateContainerId + '"</div>'
            rawdocsContentContainer.append(templateContainer);

            var hrefValue = key.replace('{id}', '?id=1');

            $('#' + templateContainerId).loadTemplate("webroot/js/templates/rawdocs-template.html",
            {
                href: hrefValue,
                url: hrefValue,
                description: dictionary[key]
            });

            // $('#list').append('<li><a href="' + hrefValue + '">Link</a>: ' + dictionary[key] +  '</li>');
        }
        
    }

    $.get('/rawdocs', getRawDocsOnSuccess);    
});