<template>	
	<view>
		<!-- 滚动导航标签 -->
		<view class="uni-tab-bar">
			<scroll-view scroll-x class="uni-swiper-tab">
				<block v-for="(tab,index) in tabBars" :key="tab.id">
					<view class="swiper-tab-list" 
					:class="{'active':tabIndex==index}"
					@tap="tabtap(index)">
						{{tab.name}}
						<view class="swiper-tab-line"></view>
					</view>
				</block>
			</scroll-view>
		</view>
		<!-- 图文，视频列表 -->
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
				tabIndex: 0,
				tabBars: [
					{ name: "关注", id: "guanzhu" },
					{ name: "推荐", id: "tuijian" },
					{ name: "体育", id: "tiyu" },
					{ name: "热点", id: "redian" },
					{ name: "财经", id: "caijing" },
					{ name: "娱乐", id: "yule" }
				],
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
			tabtap(index) {
				this.tabIndex = index;
			}
		},
		components: {
			indexList
		},
	}
</script>

<style>
	.uni-swiper-tab {
		border-bottom: 1upx solid #EEEEEE;
	}
	.swiper-tab-list {
		color: #969696;
		font-weight: bold;
	}
	.uni-tab-bar .active {
		color: #343434;
	}
	.active .swiper-tab-line {
		border-bottom: 6upx solid #FEDE33;
		width: 70upx;
		margin: auto;
		border-top: 6upx solid #FEDE33;
		border-radius: 20upx;
	}
</style>
