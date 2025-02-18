function playSongs(inputData) {
    class Song {
        constructor(title, duration) {
            this.title = title;
            this.duration = duration;
        }

        display() {
            console.log(this.title);
        }
    }

    let totalTracks = inputData.shift();
    let musicLibrary = new Map();
    let allTracks = [];

    for (let i = 0; i < totalTracks; i++) {
        let [category, title, duration] = inputData.shift().split("_");

        if (!musicLibrary.has(category)) {
            musicLibrary.set(category, []);
        }

        let newTrack = new Song(title, duration);
        musicLibrary.get(category).push(newTrack);
        allTracks.push(newTrack);
    }

    let category = inputData.shift();

    if (category === "all") {
        allTracks.forEach(track => track.display());
    } else if (musicLibrary.has(category)) {
        musicLibrary.get(category).forEach(track => track.display());
    }
}
