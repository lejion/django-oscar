var gulp = require('gulp');

['less', 'watch'].forEach(function(task) {
    require('./gulp/' + task);
});

// run default task
gulp.task('default', ['less-complete']);
