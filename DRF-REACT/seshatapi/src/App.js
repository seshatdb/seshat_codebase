import React, { useEffect, useState } from 'react';
import './App.css';
import Politys from './components/Politys';
import PolityLoadingComponent from './components/PolityLoading';

function App() {
	const PolityLoading = PolityLoadingComponent(Politys);
	const [appState, setAppState] = useState({
		loading: false,
		politys: null,
	});

	useEffect(() => {
		setAppState({ loading: true });
		const apiUrl = `http://127.0.0.1:8000/api/`;
		fetch(apiUrl)
			.then((data) => data.json())
			.then((politys) => {
				setAppState({ loading: false, politys: politys });
			});
	}, [setAppState]);
	return (
		<div className="App">
			<h1>Latest Politys</h1>
			<PolityLoading isLoading={appState.loading} politys={appState.politys} />
		</div>
	);
}
export default App;