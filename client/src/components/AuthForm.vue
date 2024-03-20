<template>
  <div class="auth-container" :style="{ width: width, height: height }">
    <p class="title"> {{ title }} </p>
    <div class="content">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AuthForm',
  props: ['title', 'width', 'height']
}
</script>

<style>
@import '@/colors.css';

.auth-container {
  margin: auto;
  position: absolute;
  top: 0; left: 0; bottom: 0; right: 0;
  border-radius: 5px;
  background-color: var(--white-1);
  box-shadow: 0 2px 5px 0 rgba(117, 106, 106, 0.5);
}

.title {
  border-radius: 5px 5px 0 0;
  text-align: center;
  background-color: var(--orange-1);
  padding: 2%;
  font-family: Inter, sans-serif;
  font-size: 24px;
  font-weight: 300;
  color: var(--grey-4);
  margin-bottom: 5%;
}

.content {
  background-color: var(--white-1);
}
</style>