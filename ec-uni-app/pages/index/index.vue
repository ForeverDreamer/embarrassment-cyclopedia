<template>	
	<view>	
		<block v-for="(item, index) in list" :key="index">
			<index-list :item="item" :index="index"></index-list>
		</block>
	</view>
</template>

<script>
	import indexList from "../../components/index/index-list.vue"
	export default {
		data() {
			return {
				list: [
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "昵称",
						isguanzhu: true,
						title: "我是标题",
						type: "img",  // img:图文, video:视频
						playnum: null, // 单位:w(万次)
						long: null,
						titlepic: "../../static/demo/datapic/11.jpg",
						infonum: {
							index: 1,  // 0:没有操作, 1:顶, 2:踩
							dingnum: 11,
							cainum: 11
						},
						commentnum: 10,
						sharenum: 10
					},
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "昵称",
						isguanzhu: false,
						title: "我是标题",
						type: "video",  // img:图文, video:视频
						playnum: "20", // 单位:w(万次)
						long: "2:47",
						titlepic: "../../static/demo/datapic/11.jpg",
						infonum: {
							index: 2,  // 0:没有操作, 1:顶, 2:踩
							dingnum: 11,
							cainum: 11
						},
						commentnum: 10,
						sharenum: 10
					}
				]
			}
		},
		onLoad() {

		},
		methods: {

		},
		components: {
			indexList
		},
	}
</script>

<style>

</style>
