<script>
    import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();

  let showForm = false;
  let itemName = '';
  let itemDescription = '';
  let itemPicture = null;
  let previewUrl = '';

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('name', itemName);
    formData.append('description', itemDescription);
    formData.append('image', itemPicture);

    const response = await fetch('http://localhost:8000/api/items-catalog/', {
      method: 'POST',
      body: formData,
    });

    if (response.ok) {
      const item = await response.json();
      console.log(item);
      dispatch('itemCreated', item);
    } else {
      console.error('Error:', response.status);
    }
  };
  const toggleForm = () => {
    showForm = !showForm;
  };

  const handleFileChange = (e) => {
    itemPicture = e.target.files[0];
    const reader = new FileReader();
    reader.onloadend = () => {
      previewUrl = reader.result;
    };
    reader.readAsDataURL(itemPicture);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    if (e.dataTransfer.items) {
      for (var i = 0; i < e.dataTransfer.items.length; i++) {
        if (e.dataTransfer.items[i].kind === 'file') {
          itemPicture = e.dataTransfer.items[i].getAsFile();
          const reader = new FileReader();
          reader.onloadend = () => {
            previewUrl = reader.result;
          };
          reader.readAsDataURL(itemPicture);
        }
      }
    }
  };
</script>

<style>
  @import '../list_with_pictures/styles.css';

</style>


<div class="item">
  {#if showForm}
    <form on:submit|preventDefault={handleSubmit}>
      <input type="text" bind:value={itemName} placeholder="Item Name" required/>
      <input type="text" bind:value={itemDescription} placeholder="Item description"/>
      <div id="drop-area">
        <p>Drag and drop a file here</p>
        <div style="display:flex;;">
          <input type="file" bind:files={itemPicture} on:change={handleFileChange}/>
          {#if previewUrl}
            <img src={previewUrl} alt="Preview"/>
          {/if}
        </div>
      </div>
      <div>
      <button type="submit">Submit</button>
      <button type="button" on:click={toggleForm}>Cancel</button>
      </div>
    </form>
  {:else}
    <button on:click={toggleForm}>Add Item</button>
  {/if}
</div>
