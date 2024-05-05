<!-- ItemList.svelte -->
<script>
  import CreateItem from "../create/CreateItem.svelte";

  import { onMount } from 'svelte';
  export let items = [];

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
  const handleItemCreated = (event) => {
    items = [...items, event.detail];
  };
    const handleItemDelete = async (itemId) => {
    try {
      const response = await fetch(`http://localhost:8000/api/items-catalog/${itemId}`, {
        method: 'DELETE',
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      // Remove the deleted item from the local items array
      items = items.filter(item => item.id !== itemId);
    } catch (error) {
      console.error('Delete error:', error);
    }
  };
</script>
<style>
  @import './styles.css';

.item-container {
  position: relative;
  display: flex;
  flex-direction: row;
  align-items: center;
}

.delete-button {
  position: absolute;
  right: 50px; /* Adjust this value to position the button from the right */
  top: 50%; /* Adjust this value to position the button from the top */
  color: red;
  cursor: pointer;
}
</style>

<section>
  {#each items as item (item.id)}
    <div class="item-container">
      <div class="item">
        {#if item.picture_url}
          <img src={item.picture_url} alt={item.name} />
        {:else}
        {/if}
          <div class="fas fa-image icon-placeholder"></div>
        <div class="text-content">
          <h2>{item.name}</h2>
          <p>{item.description}</p>
        </div>
        <i class="fas fa-times delete-button" on:click={() => handleItemDelete(item.id)}></i>
      </div>
    </div>
  {/each}
  <CreateItem on:itemCreated={handleItemCreated}/>
</section>
