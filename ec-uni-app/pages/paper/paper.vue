<template>
	<view class="body">
		<!-- 小纸条列表 -->
		<block v-for="(item, index) in list" :key="index">
			<paper-list :item="item" :index="index"></paper-list>
		</block>
	</view>
</template>

<script>
	import paperList from "../../components/paper/paper-list.vue"

	export default {
		components: {
			paperList
		},
		data() {
			return {
				list: [
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: 5
					},
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: 0
					},
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: 10
					},
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: 0
					},
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: 19
					},
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: 45
					}
				]
			}
		},
		methods: {
			
		}
	}
</script>

<style>
	.body {
		border: 1rpx solid;
		padding: 0 20rpx;
	}
</style>
