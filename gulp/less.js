var gulp = require('gulp'),
    less = require('gulp-less'),
    sourcemaps = require('gulp-sourcemaps'),
    less_task = function() {
        gulp.src('src/oscar/static/oscar/less/*.less')
            .pipe(less({
                includePaths: [
                    'src/oscar/static/less/',
                ],
                outputStyle: null,
            }))
            .pipe(sourcemaps.write('src/oscar/static/oscar/css/'))
            .pipe(gulp.dest('src/oscar/static/oscar/css/'));
    };

// used in watch task
gulp.task('less', less_task);

// used in default task
gulp.task('less-complete', [], less_task);
