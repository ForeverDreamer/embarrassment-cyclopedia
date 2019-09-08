<template>
	<view>
		
		<view class="view-box" hover-class="view-box-hover animated rubberBand" hover-stay-time="800">
			这是view
		</view>
		
		<text :selectable="true">这是text\n这是text\n这是text\n这是text\n这是text\n</text>
		
		<view class="view-box" id="view2">css选择器</view>
		
		<view class="box">
			<view>1</view>
			<view>2</view>
			<view>3</view>
		</view>
		
	</view>
	
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			
		}
	}
</script>

<style>
	
.view-box {
	width: 200upx;
	height: 200upx;
	background: #007AFF;
	color: #FFFFFF;
	margin: 100upx;
}

.view-box-hover {
	background: red;
}

#view2, text {
	background: yellow;
}

.box {
	width: 300upx;
	height: 300upx;
	background: #007AFF;
	color: #FFFFFF;
	margin: 100upx;
	padding: 50upx;
}

.box view {
	font-size: 40upx;
}

.box>view:nth-child(1) {
	font-size: 40upx;
	background: green;
}

.box>view:nth-child(2) {
	font-size: 40upx;
	background: red;
}

.box>view:nth-child(3) {
	font-size: 40upx;
	background: pink;
}

</style>
