<template>
	<view>
		<!-- 话题介绍 -->
		<topic-info :item="topicInfo"></topic-info>
	</view>
</template>

<script>
	import topicInfo from "../../components/topic/topic-info.vue"
	
	export default {
		components: {
			topicInfo
		},
		data() {
			return {
				topicInfo: {
					titlepic: "../../static/demo/topicpic/13.jpeg",
					title: "忆往事，敬余生",
					desc: "面试官：在电梯里巧遇马云你会怎么做？90后女孩的回答当初被录用",
					totalnum: 100,
					todaynum: 50
				}
			}
		},
		methods: {
			
		}
	}
</script>

<style>
</style>
