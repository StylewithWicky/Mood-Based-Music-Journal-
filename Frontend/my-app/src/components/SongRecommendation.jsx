import React from 'react'

function SongRecommendation({ song, artist, url, previewUrl }) {
  return (
    <div className="max-w-md mx-auto bg-white rounded-2xl shadow-lg overflow-hidden p-6 mt-6 border border-gray-200">
      <h2 className="text-xl font-semibold text-gray-800 mb-2">Your Vibe Match 🎵</h2>
      <p className="text-gray-600 mb-1">
        <span className="font-medium">Song:</span> {song}
      </p>
      <p className="text-gray-600 mb-3">
        <span className="font-medium">Artist:</span> {artist}
      </p>

      {previewUrl ? (
        <audio controls className="w-full mb-3">
          <source src={previewUrl} type="audio/mpeg" />
          Your browser does not support the audio element.
        </audio>
      ) : (
        <p className="text-sm text-gray-500 mb-3">No preview available.</p>
      )}

      <a
        href={url}
        target="_blank"
        rel="noopener noreferrer"
        className="inline-block text-white bg-green-500 hover:bg-green-600 font-semibold px-4 py-2 rounded-md transition"
      >
        Listen on Spotify
      </a>
    </div>
  )
}

export default SongRecommendation
