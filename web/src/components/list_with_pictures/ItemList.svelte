<!-- ItemList.svelte -->
<script>
  import CreateItem from "../create/CreateItem.svelte";

  export let items = [];
</script>
<style>
  @import './styles.css';
</style>
<section>
  <CreateItem />
  {#each items as item (item.id)}
    <div class="item">
      <img src={item.picture_url} alt={item.name} />
      <div class="text-content">
        <h2>{item.name}</h2>
        <p>{item.description}</p>
      </div>
    </div>
  {/each}
</section>
