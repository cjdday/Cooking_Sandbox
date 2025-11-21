export default function App() {
    return (
      <div className="min-h-screen bg-gray-50 flex flex-col items-center p-10">
        <h1 className="text-5xl font-bold text-gray-900 mb-4">CookBook.AI</h1>
        <p className="text-gray-600 max-w-xl text-center mb-10">
          A personal sandbox project exploring AI-generated recipes, embeddings, and cooking intelligence.
        </p>
  
        <button className="px-6 py-3 bg-green-600 text-white rounded-xl text-lg hover:bg-green-700 mb-8">
          Generate a Cookbook
        </button>
  
        <div className="flex gap-3">
          <input
            type="text"
            placeholder="Search recipes (coming soon)"
            className="px-4 py-2 border rounded-lg w-64"
          />
          <button className="px-4 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800">
            Search
          </button>
        </div>
  
        <footer className="mt-20 text-gray-500 text-sm">
          © {new Date().getFullYear()} CookBook.AI — Personal Project
        </footer>
      </div>
    );
  }
  