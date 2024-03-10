<template>
  <DataContainer
      :title="title"
      :width="containerWidth"
      :height="containerHeight"
  >
    <DataForm>
      <DataInput v-model="inputLogin" label="Почта"></DataInput>
      <DataInput v-model="inputPassword" label="Фамилия"></DataInput>
      <InfoText info="В случае проблем пишите на admin@mail ru"></InfoText>
      <DataButton title='вход'></DataButton>
    </DataForm>
  </DataContainer>
</template>

<script>
import DataContainer from "@/components/Data/DataContainer.vue";
import DataInput from "@/components/Data/DataInput.vue";
import DataForm from "@/components/Data/DataForm.vue";
import InfoText from "@/components/InfoText.vue";
import DataButton from "@/components/Data/DataButton.vue";

export default {
  name: "NotFound",
  components: {DataButton, InfoText, DataForm, DataInput, DataContainer },

  data() {
    return {
      title: 'e.moevm statistics',
      containerWidth: '31%',
      containerHeight: '45%',
      inputLogin: '',
      inputPassword: '',
    };
  },
};
</script>

<style>
</style>
