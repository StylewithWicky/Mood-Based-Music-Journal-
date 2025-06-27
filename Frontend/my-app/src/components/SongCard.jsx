import React from 'react';

function SongCard({ song, artist, url, previewUrl }) {
  return (
    <div className="mt-6 p-4 bg-gradient-to-br from-purple-600 to-indigo-600 text-white rounded-2xl shadow-lg text-center">
      <h3 className="text-xl font-bold mb-2">🎶 Your Vibe Recommendation</h3>

      <p className="text-lg">
        <span className="font-semibold">{song}</span> by <span className="italic">{artist}</span>
      </p>

      {previewUrl ? (
        <audio
          controls
          src={previewUrl}
          className="mt-4 w-full"
        >
          Your browser does not support the audio element.
        </audio>
      ) : (
        <p className="mt-2 text-sm text-gray-200">No preview available</p>
      )}

      <a
        href={url}
        target="_blank"
        rel="noopener noreferrer"
        className="mt-4 inline-block bg-white text-indigo-600 font-bold py-2 px-4 rounded-lg hover:bg-gray-200 transition"
      >
        Open in Spotify
      </a>
    </div>
  );
}

export default SongCard;
