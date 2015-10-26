var gulp = require('gulp'),
    less = require('gulp-less'),
    less_task = function() {

        gulp.src('sites/demo/static/demo/less/*.less')
            .pipe(less({
                includePaths: [
                    'src/oscar/static/less/',
                ],
                outputStyle: null,
            }))
            .pipe(gulp.dest('sites/demo/static/demo/css/'));
    };

// used in watch task
gulp.task('less', less_task);

// used in default task
gulp.task('less-complete', [], less_task);

