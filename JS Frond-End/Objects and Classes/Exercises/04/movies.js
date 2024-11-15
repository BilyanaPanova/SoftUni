function manageMovies(commands) {
    let movies = [];

    commands.forEach(command => {
        if (command.startsWith("addMovie")) {
            let movieName = command.replace("addMovie ", "");
            movies.push({ name: movieName });
        } else if (command.includes("directedBy")) {
            let [movieName, director] = command.split(" directedBy ")
            let movie = movies.find(m => m.name === movieName);
            if (movie) {
                movie.director = director;
            }
        } else if (command.includes("onDate")) {
            let [movieName, date] = command.split(" onDate ");
            let movie = movies.find(m => m.name === movieName);
            if (movie) {
                movie.date = date;
            }
        }
    });

    movies
    .filter(movie => movie.name && movie.director && movie.date) 
    .forEach(movie => console.log(JSON.stringify(movie)));

}
