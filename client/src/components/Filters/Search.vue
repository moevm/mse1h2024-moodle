<template>
  <v-text-field
      class="search-filter"
      density="compact"
      label="Поиск"
      prepend-inner-icon="mdi-magnify"
      variant="solo-filled"
      clearable
      flat
      single-line
  ></v-text-field>
</template>

<script>
export default {
  name: 'Search'
};
</script>

<style>
@import '@/colors.css';
.search-filter {
  transform: translateY(25%);
  width: 100%;
  color: var(--white-1);
}

.search-filter .v-field {
  border-radius: 7px;
  border: 1px solid var(--grey-6);
}

.search-filter .v-field__overlay {
  background-color: white;
  color: var(--grey-4);
}

.search-filter .v-field-label {
  font-size: 16px;
  font-family: Inter, sans-serif;
  font-weight: 400;
  color: var(--grey-4);
}

.search-filter .v-field__input {
  font-size: 16px;
  font-family: Inter, sans-serif;
  font-weight: 400;
  color: var(--grey-4);
}
</style>
