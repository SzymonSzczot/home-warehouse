<script>
  import { onMount } from 'svelte';

  import ItemList from '../components/list_with_pictures/ItemList.svelte';
  import CreateItem from "../components/create/CreateItem.svelte";
  let items = [];

  onMount(async () => {
    try {
      const response = await fetch('http://localhost:8000/api/items-catalog');
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      items = await response.json();
    } catch (error) {
      console.error('Fetch error:', error);
    }
  });
</script>

<svelte:head>
  <title>Home</title>
  <meta name="description" content="Warehouse"/>
</svelte:head>

<section>
    <div style= "display: flex; flex-direction: column">
        <ItemList {items} />
    </div>
</section>
